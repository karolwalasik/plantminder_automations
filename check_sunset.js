const sunset = msg.payload.astronomy.astro.sunset; // Extract sunset
const isSunUp = msg.payload.astronomy.astro.is_sun_up; // Extract is_sun_up

// Parse sunset time into a Date object
const sunsetParts = sunset.split(/[: ]/); // Split "07:36 PM" into [07, 36, PM]
const sunsetHour = parseInt(sunsetParts[0], 10);
const sunsetMinute = parseInt(sunsetParts[1], 10);
const sunsetPeriod = sunsetParts[2];

// Convert hour to 24-hour format
let sunset24Hour = sunsetHour;
if (sunsetPeriod === "PM" && sunsetHour !== 12) {
    sunset24Hour += 12;
}
if (sunsetPeriod === "AM" && sunsetHour === 12) {
    sunset24Hour = 0;
}

const currentTime = new Date(); // Current time
const sunsetTime = new Date(currentTime); // Create Date object for today's sunset
sunsetTime.setHours(sunset24Hour);
sunsetTime.setMinutes(sunsetMinute);
sunsetTime.setSeconds(0);

// Check if current time is past sunset or if the sun is down
if (currentTime > sunsetTime || isSunUp === 0) {
    // Action to close windows and blinds
    msg.payload = {
        action: "close",
        devices: ["windows", "blinds"],
        message: "Sunset detected. Closing windows and blinds."
    };
    return [msg, null]; // Pass to the first output
} else {
    // No action needed
    msg.payload = {
        action: "none",
        message: "Sun is still up. No action taken."
    };
    return [null, msg]; // Pass to the second output
}
