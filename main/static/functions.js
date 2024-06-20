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
		additionalInfo.style.display = 'flex';
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
	const plusMinus = container.querySelector(
		'#specificMembershipSectionPlusMinus'
	);

	if (!additionalInfo || !plusMinus) {
		console.error('Required elements not found.');
		return;
	}
	const currentDisplay =
		window.getComputedStyle(additionalInfo).display;
	if (currentDisplay === 'none') {
		additionalInfo.style.display = 'flex';
		plusMinus.textContent = '-';
	} else {
		additionalInfo.style.display = 'none';
		plusMinus.textContent = '+';
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
		const background = document.getElementById(
			'landingPageBackgroundPhoto'
		);
		console.log(background);
		containers.forEach((container) => {
			const originalUrl = container.getAttribute(
				'data-original-url'
			);
			const croppedUrl = container.getAttribute(
				'data-cropped-url'
			);

			if (window.innerWidth <= 800) {
				container.style.backgroundImage = `url(${originalUrl})`;
				background.style.backgroundImage = `url(${originalUrl})`;
			} else {
				container.style.backgroundImage = `url(${croppedUrl})`;
				background.style.backgroundImage = `url(${croppedUrl})`;
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
