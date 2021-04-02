import urllib.request as req
import json, sqlite3, os, time
import matplotlib.pyplot as plt
from flask import Flask, request, send_file
from flask_restx import Resource, Api, fields
from math import ceil


def create_db(db_file):
    if os.path.exists(db_file):
        print('Database already exists.')
        return False
    con = sqlite3.connect('z5274414.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE TV_Show 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tvmaze_id INTEGER,
                        last_update TEXT,
                        name TEXT,
                        type TEXT,
                        language TEXT,
                        genres TEXT,
                        status TEXT,
                        runtime INTEGER,
                        premiered TEXT,
                        officialSite TEXT,
                        schedule TEXT,
                        rating TEXT,
                        weight INTEGER,
                        network TEXT,
                        summary TEXT)''')
    con.commit()
    con.close()


app = Flask(__name__)
api = Api(app, title="TV Show", description="API for TV Show")

TV_show_model = api.model('TV Show', {
    "tvmaze_id": fields.Integer,
    "last_update": fields.String,
    "name": fields.String,
    "type": fields.String,
    "language": fields.String,
    "genres": fields.List(fields.String),
    "status": fields.String,
    "runtime": fields.Integer,
    "premiered": fields.String,
    "officialSite": fields.String,
    "schedule": fields.Raw,
    "rating": fields.Raw,
    "weight": fields.Integer,
    "network": fields.Raw,
    "summary": fields.String
})


@api.route("/tv-show/import")
@api.response(200, 'OK')
@api.response(400, 'Bad Request')
@api.response(404, 'Not Found')
@api.response(201, 'Created')
class SingleRoute(Resource):
    @api.doc(params={'name': 'name'})
    def post(self):
        name = request.args.get('name')
        name_check = name.split()
        for i in range(len(name_check)):
            name_check[i] = name_check[i].capitalize()
        check_name = ' '.join(name_check)
        print(check_name)
        a = [i for i in check_name]
        for i in range(len(a)):
            if a[i] == ' ':
                a[i] = '-'
        name_request = ''.join(a)
        print(name_request)
        resource = req.Request(f'http://api.tvmaze.com/search/shows?q={name_request}')
        data = json.loads(req.urlopen(resource).read())
        if not data:
            return {"message": "The name not found in data source!"}, 404
        data = data[0]['show']
        print(data['name'])
        if data['name'].upper() != check_name.upper():
            return {"message": "The name not found in data source!"}, 404
        con = sqlite3.connect('z5274414.db')
        cur = con.cursor()
        query = cur.execute(f"SELECT * FROM TV_Show WHERE tvmaze_id = {data['id']}").fetchall()
        if query:
            if query[0][3] != check_name:
                return {"message": "The name not found in data source!"}, 404
            return {"id": query[0][0],
                    "last-update": query[0][2],
                    "tvmaze-id": query[0][1],
                    "_links": {
                        "self": {
                            "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0]}"
                        }
                    }
                    }, 200
        else:
            information = []
            for key, value in data.items():
                if key != 'url' and key != 'webChannel' and key != 'dvdCountry' and key != 'externals' and key != 'image' and key != 'updated' and key != '_links':
                    information.append(value)
            update = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            information.insert(2, update)
            information[5] = str(information[5])
            information[10] = str(information[10])
            information[11] = str(information[11])
            information[13] = str(information[13])
            information[14] = str(information[14])
            cur.execute("INSERT INTO TV_Show (tvmaze_id,name,last_update,type,language,genres,status,runtime,"
                        "premiered,officialSite,schedule, rating,weight,network,summary) VALUES(?,?,?,?,?,?,?,?,?,?,"
                        "?,?,?,?,?)", information)
            query = cur.execute(f"SELECT * FROM TV_Show WHERE tvmaze_id = {data['id']}").fetchall()
        con.commit()
        con.close()
        return {"id": query[0][0],
                "last-update": query[0][2],
                "tvmaze-id": query[0][1],
                "_links": {
                    "self": {
                        "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0]}"
                    }
                }
                }, 201


@api.route("/tv-show/<int:id>")
@api.response(200, 'OK')
@api.response(400, 'Bad Request')
@api.response(404, 'Not Found')
class SingleRoute(Resource):
    def get(self, id):
        con = sqlite3.connect('z5274414.db')
        cur = con.cursor()
        query = cur.execute(f"SELECT * FROM TV_Show WHERE id = {id}").fetchall()
        if not query:
            return {"message": "The name not found in data source!"}, 404
        id_list = cur.execute(f"SELECT id FROM TV_Show").fetchall()
        id_list = [id_list[i][0] for i in range(len(id_list))]
        if (query[0][0] - 1) not in id_list and (query[0][0] + 1) not in id_list:
            link = {
                "self": {
                    "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0]}"
                }
            }
        elif (query[0][0] - 1) not in id_list and (query[0][0] + 1) in id_list:
            link = {
                "self": {
                    "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0]}"
                },
                "next": {
                    "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0] + 1}"
                }
            }
        elif (query[0][0] - 1) in id_list and (query[0][0] + 1) not in id_list:
            link = {
                "self": {
                    "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0]}"
                },
                "previous": {
                    "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0] - 1}"
                }
            }
        else:
            link = {
                "self": {
                    "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0]}"
                },
                "previous": {
                    "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0] - 1}"
                },
                "next": {
                    "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0] + 1}"
                }
            }
        con.commit()
        con.close()
        return {"tvmaze_id": query[0][1],
                "id": query[0][0],
                "last_update": query[0][2],
                "name": query[0][3],
                "type": query[0][4],
                "language": query[0][5],
                "genres": eval(query[0][6]),
                "status": query[0][7],
                "runtime": query[0][8],
                "premiered": query[0][9],
                "officialSite": query[0][10],
                "schedule": eval(query[0][11]),
                "rating": eval(query[0][12]),
                "weight": query[0][13],
                "network": eval(query[0][14]),
                "summary": query[0][15],
                "_links": link
                }, 200

    def delete(self, id):
        con = sqlite3.connect('z5274414.db')
        cur = con.cursor()
        query = cur.execute(f"SELECT * FROM TV_Show WHERE id = {id}").fetchall()
        if not query:
            return {"message": "The name not found in data source!"}, 404
        cur.execute(f"DELETE from TV_Show WHERE id = {id}")
        con.commit()
        con.close()
        return {f"message": f"The tv show with id {id} was removed from the database!",
                "id": id
                }, 200

    @api.expect(TV_show_model)
    def patch(self, id):
        TV_Show = request.json
        con = sqlite3.connect('z5274414.db')
        cur = con.cursor()
        query = cur.execute(f"SELECT * FROM TV_Show WHERE id = {id}").fetchall()
        update = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        if not query:
            return {"message": "The name not found in data source!"}, 404
        id_list = cur.execute(f"SELECT id FROM TV_Show").fetchall()
        id_list = [id_list[i][0] for i in range(len(id_list))]
        if (query[0][0] - 1) not in id_list and (query[0][0] + 1) not in id_list:
            link = {
                "self": {
                    "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0]}"
                }
            }
        elif (query[0][0] - 1) not in id_list and (query[0][0] + 1) in id_list:
            link = {
                "self": {
                    "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0]}"
                },
                "next": {
                    "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0] + 1}"
                }
            }
        elif (query[0][0] - 1) in id_list and (query[0][0] + 1) not in id_list:
            link = {
                "self": {
                    "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0]}"
                },
                "previous": {
                    "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0] - 1}"
                }
            }
        else:
            link = {
                "self": {
                    "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0]}"
                },
                "previous": {
                    "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0] - 1}"
                },
                "next": {
                    "href": f"http://127.0.0.1:5000/tv-shows/{query[0][0] + 1}"
                }
            }
        for key, value in TV_Show.items():
            to_str = []
            if key == 'genres' or key == 'schedule' or key == 'rating' or key == 'network':
                to_str.append(str(value))
                cur.execute(f"UPDATE TV_Show SET {key} = (?) WHERE id ={id}", to_str)
            else:
                cur.execute(f"UPDATE TV_Show SET {key} = '{value}' WHERE id ={id}")
        con.commit()
        con.close()
        return {"id": id,
                "last-update": update,
                "_links": link
                }, 200


parser = api.parser()
parser.add_argument('order_by', type=str, help='For Q5 only', location='args')
parser.add_argument('page', type=int, help='For Q5 only', location='args')
parser.add_argument('page_size', type=int, help='For Q5 only', location='args')
parser.add_argument('filter', type=str, help='For Q5 only', location='args')


@api.route("/tv-show/")
@api.response(200, 'OK')
@api.response(400, 'Bad Request')
@api.response(404, 'Not Found')
class SingleRoute(Resource):
    @api.doc(parser=parser)
    def get(self):
        a = parser.parse_args()['order_by']
        b = parser.parse_args()['page']
        c = parser.parse_args()['page_size']
        d = parser.parse_args()['filter']
        con = sqlite3.connect('z5274414.db')
        cur = con.cursor()
        query = cur.execute(f"SELECT * FROM TV_Show").fetchall()
        if ',' in a:
            a = a.split(',')
        else:
            a = [a]
        a.reverse()
        index_dict = {
            "id": 0,
            "name": 3,
            "runtime": 8,
            "premiered": 9,
            "rating-average": 12,
        }
        for i in range(len(a)):
            for j in a[i]:
                if j == '+':
                    key = a[i][1:]
                    query.sort(key=lambda x: x[index_dict[key]])
                if j == '-':
                    key = a[i][1:]
                    query.sort(key=lambda x: x[index_dict[key]], reverse=True)
                break
        all_size = len(query)
        max_page = ceil(all_size / c)
        if b > max_page:
            return {"message": "The page not found in data source!"}, 404
        if b < max_page:
            page_list = []
            for i in range((b - 1) * c, b * c):
                page_list.append(query[i])
        if b == max_page:
            page_list = query[(b - 1) * c:]
        tv_show = []
        filter_return = d
        if ',' in d:
            d = d.split(',')
        else:
            d = [d]
        filter_dict = {
            "id": 0,
            "tvmaze_id": 1,
            "last-update": 2,
            "name": 3,
            "type": 4,
            "language": 5,
            "genres": 6,
            "status": 7,
            "runtime": 8,
            "premiered": 9,
            "officialSite": 10,
            "schedule": 11,
            "rating": 12,
            "weight": 13,
            "network": 14,
            "summary": 15
        }
        for i in range(len(page_list)):
            res_dict = {}
            for j in d:
                res_dict[j] = page_list[i][filter_dict[j]]
            tv_show.append(res_dict)
        id_list = [i + 1 for i in range(max_page)]
        if (b - 1) not in id_list and (b + 1) not in id_list:
            link = {
                "self": {
                    "href": f"http://127.0.0.1:5000/tv-shows/?page={b}&page_size={c}&filter={filter_return}"
                }
            }
        elif (b - 1) not in id_list and (b + 1) in id_list:
            link = {
                "self": {
                    "href": f"http://127.0.0.1:5000/tv-shows/?page={b}&page_size={c}&filter={filter_return}"
                },
                "next": {
                    "href": f"http://127.0.0.1:5000/tv-shows/?page={b + 1}&page_size={c}&filter={filter_return}"
                }
            }
        elif (b - 1) in id_list and (b + 1) not in id_list:
            link = {
                "self": {
                    "href": f"http://127.0.0.1:5000/tv-shows/?page={b}&page_size={c}&filter={filter_return}"
                },
                "previous": {
                    "href": f"http://127.0.0.1:5000/tv-shows/?page={b - 1}&page_size={c}&filter={filter_return}"
                }
            }
        else:
            link = {
                "self": {
                    "href": f"http://127.0.0.1:5000/tv-shows/?page={b}&page_size={c}&filter={filter_return}"
                },
                "previous": {
                    "href": f"http://127.0.0.1:5000/tv-shows/?page={b - 1}&page_size={c}&filter={filter_return}"
                },
                "next": {
                    "href": f"http://127.0.0.1:5000/tv-shows/?page={b + 1}&page_size={c}&filter={filter_return}"
                }
            }
        con.commit()
        con.close()
        return {"page": b,
                "page-size": c,
                "tv-shows": tv_show,
                "_links": link
                }, 200


parser1 = api.parser()
parser1.add_argument('format', type=str, help='image or json only', location='args')
parser1.add_argument('by', type=str, help='For Q6 only', location='args')


@api.route("/tv-show/statistics")
@api.response(200, 'OK')
@api.response(400, 'Bad Request')
@api.response(404, 'Not Found')
class SingleRoute(Resource):
    @api.doc(parser=parser1)
    def get(self):
        a = parser1.parse_args()['format']
        b = parser1.parse_args()['by']
        filter_dict = {
            "type": 4,
            "language": 5,
            "genres": 6,
            "status": 7,
        }
        con = sqlite3.connect('z5274414.db')
        cur = con.cursor()
        query = cur.execute(f"SELECT * FROM TV_Show").fetchall()
        if a != 'json' and a != 'image':
            return {"message": "The value not found in data source!"}, 404
        if b not in filter_dict.keys():
            return {"message": "The value not found in data source!"}, 404
        res_list = []
        for i in range(len(query)):
            if b != "genres":
                res_list.append(query[i][filter_dict[b]])
            else:
                genres_list = eval(query[i][filter_dict[b]])
                for j in range(len(genres_list)):
                    res_list.append(genres_list[j])
        percentage_list = []
        count_res = list(set(res_list))
        for i in count_res:
            percentage_list.append(res_list.count(i))
        total = sum(percentage_list)
        for i in range(len(percentage_list)):
            percentage_list[i] = percentage_list[i] / total * 100
        value = {}
        for i in range(len(count_res)):
            value[count_res[i]] = percentage_list[i]
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        yesterday = now.replace(now[8:10], str(int(now[8:10]) - 1))
        update_list = []
        for i in range(len(query)):
            if yesterday < query[i][2] < now:
                update_list.append(query[i])
        con.commit()
        con.close()
        if a == 'image':
            plt.pie(percentage_list, labels=count_res, autopct="%.1f%%")
            plt.title(
                f'Total Number of TV shows: {len(query)}, Total Number of TV shows updated in the last 24 hours: {len(update_list)}',
                size=10)
            plt.savefig('z5274414.jpg')
            plt.close()
            filename = 'z5274414.jpg'
            return send_file(filename, mimetype='image/jpg', cache_timeout=0)
        if a == 'json':
            return {"total": len(query),
                    "total-updated": len(update_list),
                    "values": value
                    }, 200


if __name__ == '__main__':
    create_db('z5274414.db')
    app.run(debug=True)
