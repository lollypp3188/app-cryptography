function paste(id) {
  const destination = document.getElementById(id);
  navigator.clipboard
    .readText()
    .then((clipText) => (destination.value = clipText));
}


async function copy(id) {
  const sourceText = document.getElementById(id).value
  try {
    await navigator.clipboard.writeText(sourceText);
  } catch (error) {
    console.error(error.message);
  }
}