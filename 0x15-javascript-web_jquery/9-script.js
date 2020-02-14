$(document).ready(function () {
  const $hello = $('DIV#hello');
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (res) {
      $hello.text(res.hello);
    }
  });
});
