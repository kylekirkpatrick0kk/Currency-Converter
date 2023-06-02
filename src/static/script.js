document.addEventListener('DOMContentLoaded', function() {
    var convertButton = document.getElementById('fetchPriceButton');
    var btcPriceInput = document.getElementById('btcPrice');
    var goldPriceInput = document.getElementById('goldPrice');
  
    convertButton.addEventListener('click', function() {
      // Call the backend endpoint to get the BTC and gold prices
      fetch("/api/coinmarketcap/")
        .then(function(response) {
          return response.json();
        })
        .then(function(data) {
          // Display the prices in the text boxes
          btcPriceInput.value = data.btc_price;
          goldPriceInput.value = data.gold_price
        })
        .catch(function(error) {
          console.log(error);
        });
    });
  });
  