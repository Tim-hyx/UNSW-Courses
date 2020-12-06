import logo from '../assets/logo.png'

const headerstyle = {
    height: '80px',
    width: '100%',
    backgroundColor: '#eeeeee',

}

const imgstyle = {
    width: '50px',
    height: '50px',
    margin: '15px'
}


const Naviation = () => {

    return (
        <div>
            <header style={headerstyle}>
                <img style={imgstyle} src={logo} alt={'logo'}/>
                <span style={{position: 'absolute', top: '30px', left: '80%'}}><a
                    href={'/'}>Home</a> | <a
                    href={'/Blanko'}>Blanko</a> | <a
                    href={'/Slido'}>Slido</a> | <a
                    href={'/Tetro'}>Tetro</a></span>
            </header>
        </div>
    );
}
export default Naviation;