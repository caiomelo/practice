if (Meteor.isClient) {
  // counter starts at 0
  Session.setDefault('counter', 0);
  Session.setDefault('name', 'User')

  Template.hello.helpers({
    counter: function () {
      return Session.get('counter');
    }
  });

  Template.hello.helpers({
    name: function () {
      return Session.get('name');
    }
  });

  Template.hello.events({
    'click button': function () {
      // increment the counter when button is clicked
      Session.set('counter', Session.get('counter') + 1);
    }
  });

  Template.addname.events({
    'submit .save-name-form': function(e) {
      e.preventDefault();
      $form = $(e.currentTarget);
      var name = $form.find('[name="name"]').val()
      Session.set('name', name)
      Session.set('counter', 0);
    }
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
