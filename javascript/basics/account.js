let myAccount = {
    name: 'Groot',
    expenses: 0,
    income: 0
}

let addExpense = function (account, amount) {
    account.expenses = account.expenses + amount
}

let addIncome = function (account, amount) {
    account.income = account.income + amount;
}

let resetAccount = function (account) {
    account.expenses = 0;
    account.income = 0;
}

let getSummary = function (account) {
    return `${account.name}'s income is $${account.income} and expense is $${expenses}.`
}

addIncome(myAccount,250)
console.log(myAccount.income)