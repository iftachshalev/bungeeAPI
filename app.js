// !requires! >>>>>>>
const express             = require("express"),
	app                   = express(),
	bodyParser            = require("body-parser"),
	mongoose              = require('mongoose'),
	methodOverride        = require("method-override");
// <<<<<<<< !requires!

// !setup! >>>>>>>>>>

// set mongoose up
mongoose.set('useFindAndModify', false);
mongoose.connect('mongodb://localhost:27017/yelp_camp', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to DB!'))
.catch(error => console.log(error.message));

// set body parser and view engine
app.use(bodyParser.urlencoded({extended: true}));
app.set("view engine", "ejs");
app.use(express.static(__dirname + "/public"));
app.use(methodOverride("_method"));
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
// <<<<<<<<<< !setup!

app.get("/" (req, res) => res.send("sert"))