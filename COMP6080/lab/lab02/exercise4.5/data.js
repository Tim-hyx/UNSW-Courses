const numbers = [406, 646, 199, 996, 989, 47, 55, 614, 293, 407, 287, 605, -56, 960, 832, 25, 596, 541, -577, 56, 878, 483, 681, 17, 73, 428, -757, 923, 748, 619, 117, 588, -661, -267, 571, 95, 923, 386, 507, 243, -868, -797, 344, 660, 34, 945, -424, -169, 344, 601, 277, 478, 562, 863, 887, 172, 23, 995, 999, 2, 12, 476, 755, 617, 155, 698, 91, 1, 481, 971, 371, 164, 220, 854, 590, 364, 446, 254, 980, 469, 738, 866, 297, 410, 407, 576, 893, 319, 866, 501, 939, 536, 380, 331, 438, 76, 423, 951, 459, 425];

function negative(numbers) {
    const negative_list = [];
    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] < 0) {
            negative_list.push(numbers[i])
        }
    }
    negative_list.sort(function (a, b) {
        return a - b
    })
    return negative_list
}

function average(numbers) {
    let sum = 0;
    let count = 0;
    for (let i = 0; i < numbers.length; i++) {
        if ((numbers[i] > 0) && (numbers[i] % 6 === 0)) {
            sum += numbers[i];
            count += 1;
        }
    }
    let result = sum / count;
    result = result.toFixed(1);
    return result;
}

function large(numbers) {
    const large_list = [];
    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] > 600) {
            large_list.push(numbers[i])
        }
    }
    large_list.reverse()
    return large_list
}

console.log('List of negatives = [' + negative(numbers) + ']')
console.log('Average of positive numbers 6 divisible = ' + average(numbers))
console.log('List of large numbers in reverse = [' + large(numbers) + ']')