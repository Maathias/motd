const { exec } = require('child_process')

module.exports = function ex(com) {
	return new Promise((resolve, reject) => {
		exec(com, (err, stdout, stderr) => {
			if (stderr) reject(stderr)
			resolve(stdout)
		})
	})
}