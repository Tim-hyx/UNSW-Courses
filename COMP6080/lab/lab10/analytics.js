let data = require('./HC.json');
/* Complete the function `biggestGrowth` such that it returns the name of
   the school that has had the largest growth (increase) of students between 2004 and
   2018 (i.e. find the school where difference between the 2018 HC and 2004
   HC is the largest, ignoring anything that happened in years 2005-2017). */
const biggestGrowth = () => {
    let growth_list = [];
    for (let i = 0; i < data.length; i++) {
        if (!isNaN(parseInt(data[i]['HC_2018'])) && (!isNaN(parseInt(data[i]['HC_2004'])))) {
            let growth = parseInt(data[i]['HC_2018']) - parseInt(data[i]['HC_2004']);
            growth_list.push(growth);
        } else growth_list.push(0)
    }
    let max_school_name_list = [];
    let max_school = Math.max(...growth_list);
    for (let j = 0; j < growth_list.length; j++) {
        if (growth_list[j] === max_school) {
            max_school_name_list.push(data[j]['School Name']);
        }
    }
    max_school_name_list.sort();
    console.log(max_school_name_list[0]);
    return max_school_name_list[0]; // TODO
};

/* Complete the function `overallHeadCount` such that it returns the name of
   the school that has the largest sum of all of the head counts across all
   of the years that the school lists for. This function returns a string. */
const overallHeadCount = () => {
    let sum_list = [];
    for (let i = 0; i < data.length; i++) {
        let num = [];
        for (let j = 0; j < 15; j++) {
            if (!isNaN(parseInt(data[i][`HC_${2004 + j}`]))) {
                num.push(parseInt(data[i][`HC_${2004 + j}`]));
            }
        }
        sum_list.push(num.reduce((a, b) => a + b, 0));
    }
    let sum_school = Math.max(...sum_list);
    let sum_school_name_list = [];
    for (let j = 0; j < sum_list.length; j++) {
        if (sum_list[j] === sum_school) {
            sum_school_name_list.push(data[j]['School Name']);
        }
    }
    sum_school_name_list.sort();
    console.log(sum_school_name_list[0]);
    return sum_school_name_list[0]; // TODO
};

/* Complete the function `largestVariation` such that it returns the name of
   the school that has the largest variation in head count between adjacent
   years. E.G. If a school has a HC in 2005 of 78, and then a HC in 2006 of
   88, then that is a variation of 10. It does not matter if the variation
   goes up or down. This function returns a string. */
const largestVariation = () => {
    let variation_list = [];
    for (let i = 0; i < data.length; i++) {
        let every_school_variation = [];
        for (let j = 0; j < 14; j++) {
            if (!isNaN(parseInt(data[i][`HC_${2004 + j}`])) && !isNaN(parseInt(data[i][`HC_${2004 + j + 1}`]))) {
                let variation = parseInt(data[i][`HC_${2004 + j + 1}`]) - parseInt(data[i][`HC_${2004 + j}`])
                every_school_variation.push(Math.abs(variation));
            } else every_school_variation.push(0)
        }
        variation_list.push(Math.max(...every_school_variation));
    }
    let max_variation = Math.max(...variation_list);
    let variation_school_name_list = [];
    for (let j = 0; j < variation_list.length; j++) {
        if (variation_list[j] === max_variation) {
            variation_school_name_list.push(data[j]['School Name']);
        }
    }
    variation_school_name_list.sort();
    console.log(variation_school_name_list[0]);
    return variation_school_name_list[0]; // TODO
};

module.exports = {
    biggestGrowth,
    overallHeadCount,
    largestVariation,
}