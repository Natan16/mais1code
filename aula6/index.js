$.ajax({
    headers: { 'X-Auth-Token': '3b9afb37094b4c00a69322c88f3edd89' },
    url: 'http://api.football-data.org/v2/matches/?dateFrom=2022-07-03&dateTo=2022-07-10',
    dataType: 'json',
    type: 'GET',
  }).done(function(response) {
    for(var i in response["matches"]) {
      $('#showresults').append("<img width='32px' src="+ response["matches"][i]["competition"]["area"]["ensignUrl"] + ">")
      $('#showresults').append("<span>"+response["matches"][i]["competition"]["name"]+":</span><br>")
      $('#showresults').append("<span>"+response["matches"][i]["awayTeam"]["name"]+"</span>")
      $('#showresults').append("<span>("+response["matches"][i]["score"]["fullTime"]["awayTeam"]+")-</span>")
      $('#showresults').append("<span>"+response["matches"][i]["homeTeam"]["name"]+"</span>")
      $('#showresults').append("<span> ("+response["matches"][i]["score"]["fullTime"]["homeTeam"]+")</span><br><br>")
    }
    // usar o clone e o appendTo
      console.log(response);
  });
