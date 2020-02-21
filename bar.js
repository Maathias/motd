module.exports = function bar(used, total, chars = ['#', '-'], max = 40) {

	var percent = used / total,
		len = Math.round(percent * max),
		rest = max - len

	percent = (percent * 100).toFixed(1)
	return ` ${percent}%${' '.repeat(6-percent.length)}[${chars[0].repeat(len)}\x1b[0m${chars[1].repeat(rest)}\x1b[0m]    `
}