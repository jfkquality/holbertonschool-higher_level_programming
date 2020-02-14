$(document).ready(function () {
  const $hello = $('DIV#hello');
  $('INPUT#btn_translate').click(function () {
    const $lang = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=' + $lang,
      success: function (res) {
        $hello.text(res.hello);
      }
    });
  });
});
