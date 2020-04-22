

var switcher=function(){
    var ID=$(this).attr('id');
    $('#ajax-content').load('./'+ID);
    $("#recipedisplay, .btn-outline-success.active").toggleClass('active');
    $("#"+ID).addClass('active');
};



$('#fav').on('click',switcher);
$('#history').on('click',switcher);

$('document').ready(function() {
    $('#ajax-content').load('./fav');
    $("#fav").addClass('active');
});









