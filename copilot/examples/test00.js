function calculateDaysBetweenDays(startDate, endDate) {
	var startDate = new Date(startDate);
	var endDate = new Date(endDate);

	var millisecondsPerDay = 1000 * 60 * 60 * 24;
	
	var startDateInMilliseconds = startDate.getTime();
	var endDateInMilliseconds = endDate.getTime();
	
	var daysBetween = (endDateInMilliseconds - startDateInMilliseconds) / millisecondsPerDay;
	
	return daysBetween;
}