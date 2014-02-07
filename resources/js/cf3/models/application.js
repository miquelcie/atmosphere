define(['underscore', 'models/base'], function(_, Base) {

    var Application = Base.extend({
        defaults: { 'model_name': 'application' },
        parse: function(response) {
            var attributes = response;
            attributes.id = response.uuid;
            return attributes;
        },
        url: function(){
            var url = this.urlRoot
                + '/' + this.defaults.model_name + '/';
            
            if (typeof this.get('id') != 'undefined') {
                url += this.get('id') + '/';
            }
            
            return url;
        }
    });

    _.extend(Application.defaults, Base.defaults);

    return Application;
});
