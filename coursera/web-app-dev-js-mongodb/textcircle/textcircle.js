this.Documents = new Mongo.Collection("documents");
EditingUsers = new Mongo.Collection("editingUsers");

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
        return configEditor;
    },

    });

    Template.editingUsers.helpers({
        users:function() {
            var doc, eusers, users;

            doc = Documents.findOne();
            if (!doc) {return;}

            eusers = EditingUsers.findOne({docId:doc._id});
            if (!eusers) {return;}

            var i = 0;
            users = new Array();

            for (var user_id in eusers.users) {
                users[i] = eusers.users[user_id];
                i++;
            }

            return users;
        }
    });

}

if (Meteor.isServer) {
    Meteor.startup(createNewDoc);
}

Meteor.methods({
    addEditingUser:function() {
        var user, doc;
        doc = Documents.findOne();
        if(!doc) {return;}
        if(!this.userId) {return;}
        user = Meteor.user().profile;
        eusers = EditingUsers.findOne({docId:doc._id});

        if (!eusers) {
            eusers = {
                docId:doc._id,
                users:{

                }
            };
        }
        user.lastEdit = new Date();
        eusers.users[this.userId] = user;
        EditingUsers.upsert({_id:eusers._id}, eusers);
    }
})

//Creates a new document to be edited, if it doesn't exist yet
function createNewDoc() {
    if(!Documents.findOne()) {
        var newDocument = {title: "new doc", author:"Caio"};
        Documents.insert(newDocument);
    }
}

//Adds a listener for the editor's changes
function configEditor(editor) {
    editor.setOption("lineNumbers", true);
    editor.setOption("theme", "cobalt");
    editor.setOption("mode", "html");
    editor.on("change", showCurrValue);
}

//Gets the content of the preview_iframe and adds the cm_editor content to it as html
function showCurrValue(cm_editor, info) {
  $("#preview_iframe").contents().find("html").html(cm_editor.getValue());
  Meteor.call("addEditingUser");
}
