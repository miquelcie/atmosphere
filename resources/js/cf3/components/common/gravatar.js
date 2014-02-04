define(['react', 'profile'], function(React, profile) {

    var Icon = React.createClass({
        getDefaultProps: function() {
            return {
                type: profile.get('settings')['icon_set']
            };
        },
        propTypes: {
            hash: React.PropTypes.string
        },
        getSrc: function(hash, icon_set) {
            switch (icon_set) {
                case 'unicorn':
                    return "//unicornify.appspot.com/avatar/" + hash + "?s=50";
                case 'wavatar':
                    return "//www.gravatar.com/avatar/" + hash + "?d=wavatar&s=50";
                case 'monster':
                    return "//www.gravatar.com/avatar/" + hash + "?d=monsterid&s=50";
                case 'retro':
                    return "//www.gravatar.com/avatar/" + hash + "?d=retro&s=50";
                case 'robot':
                    return "//robohash.org/" + hash + "?size=50x50";
                default:
                    return "//www.gravatar.com/avatar/" + hash + "?d=identicon&s=50"; 
            }
        },
        render: function() {
            /* If a type is specified in props, use it. Otherwise, use the 
             * profile setting 
             */
            return React.DOM.img({src: this.getSrc(this.props.hash, this.props.type)});
        }
    });

    return Icon;

});