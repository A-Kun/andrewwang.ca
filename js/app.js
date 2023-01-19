$(document).foundation();

function nyan() {
  if ($('#nyan').html()) {
    $('#nyan').html('');
  } else {
    $('#nyan').html('<iframe src="http://www.nyan.cat/index.php?cat=original" style="display: none;"></iframe>');
  }
}
