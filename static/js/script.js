/**
 * Created by 冯晓 on 2017/2/17.
 */
$(function () {
    $('body').scrollspy({ target: '#myScrollspy' });

    function search_click(){
        var keywords = $('.form-control').val(),
            request_url = '';
        if(keywords == ""){
            return
        }
        request_url = "/blog/Search/?keywords="+keywords;
        window.location.href = request_url
    }

    $('#search').click(function () {

        search_click();
    })


});