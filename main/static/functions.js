// JavaScript to toggle navbar items when hamburger button is clicked
function menuToggle() {
	document.getElementById('menu').classList.toggle('show');
	document.body.classList.toggle('menu-open');
	document
		.getElementById('navbar-toggle')
		.classList.toggle('change');
}
function displayMembershipInfo(button) {
	const additionalInfo =
		button.parentElement.nextElementSibling;
	if (
		additionalInfo.style.display === 'none' ||
		additionalInfo.style.display === ''
	) {
		additionalInfo.style.display = 'block';
		button.textContent = '-';
	} else {
		additionalInfo.style.display = 'none';
		button.textContent = '+';
	}
}

function displayMembershipInfoFromDiv(container) {
	const additionalInfo = container.querySelector(
		'.membershipAdditionalInfo'
	);
	if (
		additionalInfo.style.display === 'none' ||
		additionalInfo.style.display === ''
	) {
		additionalInfo.style.display = 'block';
	} else {
		additionalInfo.style.display = 'none';
	}
}

function setFooterYear() {
	const yearElement =
		document.getElementById('footer-year');
	const currentYear = new Date().getFullYear();
	yearElement.textContent = currentYear;
}
window.onload = setFooterYear;

document.addEventListener('DOMContentLoaded', function () {
	function updateBackgroundImages() {
		const containers = document.querySelectorAll(
			'.specificTrainingContainer'
		);
		containers.forEach((container) => {
			const originalUrl = container.getAttribute(
				'data-original-url'
			);
			const croppedUrl = container.getAttribute(
				'data-cropped-url'
			);

			if (window.innerWidth <= 800) {
				container.style.backgroundImage = `url(${originalUrl})`;
			} else {
				container.style.backgroundImage = `url(${croppedUrl})`;
			}
		});
	}

	// Update background images on initial load
	updateBackgroundImages();

	// Update background images on window resize
	window.addEventListener(
		'resize',
		updateBackgroundImages
	);
});
