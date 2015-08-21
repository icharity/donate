;(function() {
    $(document).ready(function() {
        $('.title .like').click(function() {
            $(this).toggleClass('active');
            if($(this).hasClass('active')) {
                $(this).parent().find('.animation-number').fadeIn('slow');
                $(this).parent().find('.animation-number').fadeOut('slow');
            }
        });

        $('.selectpicker').selectpicker();
    });
})();