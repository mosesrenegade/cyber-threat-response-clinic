var mongoose = require('mongoose');

var Schema = mongoose.Schema;

var SessionIdSchema = new Schema(
    {
	sessionId: { type: Number, required: true, max: 6 }
    }
);

SessionIdSchema
    .virtual('url')
    .get(function () {
	return '/api/sessionid/' + this._id;
    });
	 
module.exports = mongoose.model('SessionId', SessionIdSchema);
