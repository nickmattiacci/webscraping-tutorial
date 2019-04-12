const request = require('request'); // import library for sending HTTP requests
const cheerio = require('cheerio'); // import library for parsing HTML

request('http://books.toscrape.com', (err, resp, body) => {
	if (err || resp.statusCode !== 200) {
		console.log('Error getting website');
	} else {
		let $ = cheerio.load(body);
		$('article').each((index, element) => {
			let title = $('h3', element).text();
			let price = $('p.price_color', element).text();
			console.log('Title: ', title);
			console.log('Price: ', price);
			console.log('---------------');
		});
	}
});