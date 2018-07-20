#!/usr/bin/env node

console.log('Fake Session IDs')

var userArgs = process.argv.slice(2);
if (!userArgs[0].startsWith('mongodb://')) {
    console.log('ERROR!: Provide me a mongodb:// url link');
    return
}

var async = require('async');
var sessionId = require('../models/sessionid');

var mongoose = require('mongoose');
var mongoDB = userArgs[0];
mongoose.connect(mongoDB);
mongoose.Promise = global.Promise;
var db = mongoose.connection;
mongoose.connection.on('error', console.error.bind(console, 'MongoDB connection error:'));

var sessionIds = []

function sessionIdCreate(sid, cb) {
    sessiondetail = { sessionId:sid }

    var sessid = new SessionId(sessiondetail);

    sessid.save(function (err) {
	if (err) {
	    cb(err, null);
	    return;
	}
	console.log('New session: ' + sid);
	sessionIds.push(sessid)
	cb(null, sessid)
    });
}

function createSessionIds(cb) {
    async.parallel([
	function(callback) {
            sessionIdCreate(123456, callback);
	},
	function (callback) {
      	    sessionIdCreate(654321, callback);
        },
        ],
        cb);
}

async.series([
    createSessionIds
],
	     function(err, results) {
		 if (err) {
		     console.log('Finall Err:' + err);
		 }
		 else {
		     console.log('SessionIds: ' + sessionIds);
		 }
		 mongoose.connection.close();
	     });

	     
		     
		     
		     
	     
	
	    
