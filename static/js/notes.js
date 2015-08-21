;(function() {
    $(document).ready(function() {
        $('.title .like').click(function() {
            $(this).toggleClass('active');
            if($(this).hasClass('active')) {
                $(".panel-body .animation-number").fadeIn();
                $(".panel-body .animation-number").fadeOut();
            }

        });
    });
})();