document.addEventListener('DOMContentLoaded', function() {
  var convertButton = document.getElementById('fetchPriceButton');
  var btcPriceInput = document.getElementById('btcPrice');
  var goldPriceInput = document.getElementById('goldPrice');
  var convertFromValueInput = document.getElementById('convertFromValue');
  var convertFromUnitSelect = document.getElementById('convertFromUnit');
  var convertToValueInput = document.getElementById('convertToValue');
  var convertToUnitSelect = document.getElementById('convertToUnit');

  convertButton.addEventListener('click', function() {
    // Call the backend endpoint to get the BTC and gold prices
    fetch("/api/coinmarketcap/")
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        // Display the prices in the text boxes
        btcPriceInput.value = data.btc_price;
        goldPriceInput.value = data.gold_price;
      })
      .catch(function(error) {
        console.log(error);
      });
  });

  function convertCurrency() {
    var convertFromValue = parseFloat(convertFromValueInput.value);
    var convertFromUnit = convertFromUnitSelect.value;
    var convertToUnit = convertToUnitSelect.value;
    var btcPrice = parseFloat(btcPriceInput.value);
    var goldPrice = parseFloat(goldPriceInput.value);
    var dollarToBtcRate = 1 / btcPrice;
    var dollarToGoldRate = 1 / goldPrice;

    var convertedValue;

    if (convertFromUnit === 'gold' && convertToUnit === 'btc') {
      convertedValue = (convertFromValue * goldPrice / btcPrice).toFixed(8);
    } else if (convertFromUnit === 'gold' && convertToUnit === 'dollar') {
      convertedValue = (convertFromValue * goldPrice).toFixed(2);
    } else if (convertFromUnit === 'btc' && convertToUnit === 'gold') {
      convertedValue = (convertFromValue * btcPrice / goldPrice).toFixed(2);
    } else if (convertFromUnit === 'btc' && convertToUnit === 'dollar') {
      convertedValue = (convertFromValue * dollarToBtcRate).toFixed(2);
    } else if (convertFromUnit === 'dollar' && convertToUnit === 'gold') {
      convertedValue = (convertFromValue * dollarToGoldRate).toFixed(2);
    } else if (convertFromUnit === 'dollar' && convertToUnit === 'btc') {
      convertedValue = (convertFromValue * dollarToBtcRate).toFixed(8);
    } else {
      // If the units are the same, set the converted value equal to the entered value
      convertedValue = convertFromValue;
    }

    convertToValueInput.value = convertedValue;
  }

  convertFromValueInput.addEventListener('input', convertCurrency);
  convertFromUnitSelect.addEventListener('change', convertCurrency);
  convertToUnitSelect.addEventListener('change', convertCurrency);
});
