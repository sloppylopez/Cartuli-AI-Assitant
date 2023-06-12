function simulateClick(element) {
  const event = new MouseEvent('click', {
    bubbles: true,
    cancelable: true,
    view: window
  });

  element.dispatchEvent(event);
}

function measureClickTime(element) {
  const startTime = performance.now();

  return new Promise(resolve => {
    element.addEventListener('click', () => {
      const endTime = performance.now();
      const duration = endTime - startTime;
      const status = element.innerText ? 'Success' : 'No response';

      resolve({ duration, status });
    }, { once: true });

    simulateClick(element);
  });
}

function clickAllElements() {
  const clickableElements = document.querySelectorAll('a, button, input[type="button"], input[type="submit"], [role="button"], [onclick]');
  const promises = [];

  clickableElements.forEach(element => {
    promises.push(measureClickTime(element));
  });

  Promise.all(promises).then(results => {
    console.log(results);
  });
}

// Execute the click simulation
clickAllElements();
