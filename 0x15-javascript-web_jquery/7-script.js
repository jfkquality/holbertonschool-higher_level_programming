$(function () {
  let $divChar = $('DIV#character');
  $.ajax({
    type: 'GET',
    url: 'https://swapi.co/api/people/5/?format=json',
    success: function (res) {
      $divChar.text(res.name);
    }
  });
});
