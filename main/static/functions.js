// JavaScript to toggle navbar items when hamburger button is clicked
function menuToggle() {
	document.getElementById('menu').classList.toggle('show');
	document.body.classList.toggle('menu-open');
	document.getElementById('navbar-toggle').classList.toggle('change');
}
function displayMembershipInfo(button) {
	const additionalInfo = button.parentElement.nextElementSibling;
	if (additionalInfo.style.display === 'none' || additionalInfo.style.display === '') {
		additionalInfo.style.display = 'flex';
		button.textContent = '-';
	} else {
		additionalInfo.style.display = 'none';
		button.textContent = '+';
	}
}

function displayMembershipInfoFromDiv(container) {
	const additionalInfo = container.querySelector('.membershipAdditionalInfo');
	const plusMinus = container.querySelector('#specificMembershipSectionPlusMinus');

	if (!additionalInfo || !plusMinus) {
		console.error('Required elements not found.');
		return;
	}
	const currentDisplay = window.getComputedStyle(additionalInfo).display;
	if (currentDisplay === 'none') {
		additionalInfo.style.display = 'flex';
		plusMinus.textContent = '-';
	} else {
		additionalInfo.style.display = 'none';
		plusMinus.textContent = '+';
	}
}

function setFooterYear() {
	const yearElement = document.getElementById('footer-year');
	const currentYear = new Date().getFullYear();
	yearElement.textContent = currentYear;
}
window.onload = setFooterYear;

document.addEventListener('DOMContentLoaded', function () {
	function updateBackgroundImages() {
		const containers = document.querySelectorAll('.specificTrainingContainer');

		containers.forEach((container) => {
			const originalUrl = container.getAttribute('data-original-url');
			const croppedUrl = container.getAttribute('data-cropped-url');

			if (window.innerWidth <= 800) {
				container.style.backgroundImage = `url(${originalUrl})`;
			} else {
				container.style.backgroundImage = `url(${croppedUrl})`;
			}
		});
	}

	function updateLandingPageImages() {
		const backgrounds = document.querySelectorAll('.landingPageBackgroundPhoto');
		backgrounds.forEach((background) => {
			const originalUrl = background.getAttribute('data-original-url');
			const croppedUrl = background.getAttribute('data-cropped-url');

			if (window.innerWidth <= 800) {
				background.style.backgroundImage = `url(${originalUrl})`;
			} else {
				background.style.backgroundImage = `url(${croppedUrl})`;
			}
		});
	}

	function updateEventsImages() {
		const events = document.querySelectorAll('.singleEventImage');
		events.forEach((background) => {
			const originalUrl = background.getAttribute('data-original-url');
			const croppedUrl = background.getAttribute('data-cropped-url');

			if (window.innerWidth <= 800) {
				background.style.backgroundImage = `url(${originalUrl})`;
			} else {
				background.style.backgroundImage = `url(${croppedUrl})`;
			}
		});
	}

	// Update background images on initial load
	updateBackgroundImages();
	updateLandingPageImages();
	updateEventsImages();

	// Update background images on window resize
	window.addEventListener('resize', updateBackgroundImages, updateLandingPageImages, updateEventsImages);
});

function copyToClipboard() {
	// Get the text field

	// Copy the text inside the text field
	navigator.clipboard.writeText('11507 120 St NW #200 Edmonton, AB T5G 2Y2');

	// Alert the copied text
	alert('Copied the text: ' + '11507 120 St NW #200 Edmonton, AB T5G 2Y2');
}

document.getElementById('locationCopyBtn').addEventListener('click', function () {
	copyToClipboard();
});

function copyToClipboard() {
	const textToCopy = '11507 120 St NW #200 Edmonton, AB T5G 2Y2';

	// Check if the clipboard API is available
	if (navigator.clipboard) {
		navigator.clipboard
			.writeText(textToCopy)
			.then(() => {
				alert('Copied the text: ' + textToCopy);
			})
			.catch((err) => {
				console.error('Failed to copy text: ', err);
				alert('Failed to copy text.');
			});
	} else {
		// Fallback for older browsers
		const textArea = document.createElement('textarea');
		textArea.value = textToCopy;
		textArea.style.position = 'fixed'; // Avoid scrolling to bottom of page in MS Edge.
		document.body.appendChild(textArea);
		textArea.focus();
		textArea.select();
		try {
			document.execCommand('copy');
			alert('Copied the text: ' + textToCopy);
		} catch (err) {
			console.error('Fallback: Oops, unable to copy', err);
			alert('Failed to copy text.');
		}
		document.body.removeChild(textArea);
	}
}
