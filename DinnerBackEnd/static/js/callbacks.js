// Callback Functions

function input_onchange(obj, method) {
  let id = obj.id;

  if (obj.tagName !== "INPUT") {
    console.error("Incorrect Tag Callback by " + id);
    return -1;
  }

  let value = obj.value;

  console.info("Committed " + value + " by " + id);

  if (!method) {
    console.error("Undefined Method is Called");
    return -2;
  }

  method(value);

  return 0;
}
