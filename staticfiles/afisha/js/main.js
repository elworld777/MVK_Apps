var activ;

$("body").on("click", function () {
  clearTimeout(activ);
  activ = setTimeout(function () {
    window.location.href = "/afisha";
  }, 600000);
});