this.Documents = new Mongo.Collection("documents");

if (Meteor.isClient) {

  Template.editor.helpers({
    docid:function() {
      var doc = Documents.findOne();
      if(doc) {
        return doc._id;
      } else {
        return undefined;
      }
    },

    config:function() {
      return addListener;
    },

  });

}

if (Meteor.isServer) {
  Meteor.startup(createNewDoc);
}

//Creates a new document to be edited, if it doesn't exist yet
function createNewDoc() {
  if(!Documents.findOne()) {
    var newDocument = {title: "new doc", author:"Caio"};
    Documents.insert(newDocument);
  }
}

//Adds a listener for the editor's changes
function addListener(editor) {
  editor.on("change", showCurrValue);
}

//Gets the content of the preview_iframe and adds the cm_editor content to it as html
function showCurrValue(cm_editor, info) {
  $("#preview_iframe").contents().find("html").html(cm_editor.getValue());
}
