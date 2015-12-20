this.Documents = new Mongo.Collection("documents");

if (Meteor.isClient) {

  //Sets an interval of 1000ms between the executions of the specified function
  Meteor.setInterval(setCurrentDate, 1000);


  Template.date_display.helpers({
    current_date:function() {
      return Session.get("current_date");
    }
  });

  Template.editor.helpers({
    docid:function() {
      var doc = Documents.findOne();
      if(doc) {
        return doc._id;
      } else {
        return undefined;
      }
    }
  });

}

if (Meteor.isServer) {
  Meteor.startup(createNewDoc);
}

  //Sets the value of the current_date session variable with the current date and time
  function setCurrentDate() {
      Session.set("current_date", new Date());
  }

  //Creates a new document to be edited, if it doesn't exist yet
  function createNewDoc() {
    if(!Documents.findOne()) {
      var newDocument = {title: "new doc", author:"Caio"};
      Documents.insert(newDocument);
    }
  }
