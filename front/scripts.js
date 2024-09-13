const priceMinInput = document.querySelector('input[name="price-min"]')
const priceMaxInput = document.querySelector('input[name="price-max"]')

const priceMinValue = document.querySelector('#price-min-value')
const priceMaxValue = document.querySelector('#price-max-value')


priceMinValue.textContent = priceMinInput.value
priceMaxValue.textContent = priceMaxInput.value


priceMinInput.addEventListener('input', event => {
    priceMinValue.textContent = event.target.value
})

priceMaxInput.addEventListener('input', event => {
    priceMaxValue.textContent = event.target.value
})

