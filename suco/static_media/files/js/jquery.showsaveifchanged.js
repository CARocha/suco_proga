;(function ( $, window, document, undefined ) {

    // Create the defaults once
    var pluginName = 'showsaveifchanged',
        defaults = {
            propertyName: "value"
        };

    // The actual plugin constructor
    function Plugin( element, options ) {
        this.element = element;
        this.options = $.extend( {}, defaults, options) ;
        this._defaults = defaults;
        this._name = pluginName;
        this.init();
    }

    Plugin.prototype.init = function () {
        // Place initialization logic here
        // You already have access to the DOM element and
        // the options via the instance, e.g. this.element
        // and this.options
        var $elem = $(this.element);
        $('.showsaveifchanged_button').hide();
        var $button = $elem.next(".showsaveifchanged_button");

        var initialvalue = $elem.val();
        var initialmd5 = "";
        if (initialvalue != "") {
            initialmd5 = $().crypt({method:"md5",source:initialvalue});
        }

        $elem.attr('data-initialmd5', initialmd5);

        $elem.bind('input', function()
        {

            if(typeof (entry_timeout) != "undefined") {
                clearTimeout(entry_timeout);
            }

            entry_timeout = setTimeout(function() {
                entry_timeout = undefined;

                currentmd5 = $elem.attr('data-initialmd5');

                newval = $elem.val();
                if (newval == "")
                {
                    newmd5 = "";
                } else {
                    newmd5 = $().crypt({method:"md5",source:newval});
                }

                if (currentmd5 == newmd5)
                {
                    $button.hide();
                } else {
                    $button.fadeIn('fast');
                }
            }, 10);

        });
    };

    // A really lightweight plugin wrapper around the constructor,
    // preventing against multiple instantiations
    $.fn[pluginName] = function ( options ) {
        return this.each(function () {
            if (!$.data(this, 'plugin_' + pluginName)) {
                $.data(this, 'plugin_' + pluginName,
                new Plugin( this, options ));
            }
        });
    }

})( jQuery, window, document );