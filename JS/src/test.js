compose = (...fns) => (a, b) => {
    fns.reduce((composed, fn2) => fn2() )

}

add = (a, b) => a + b
multiply = (a , b) => a * b


compose(add, multiply)