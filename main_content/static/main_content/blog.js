// Handle category selection and load subcategories
document
  .getElementById("category-select")
  .addEventListener("change", function () {
    var categoryName = this.value;

    // Clear subcategory select and form fields
    var subcategorySelect = document.getElementById("subcategory-select");
    subcategorySelect.innerHTML =
      '<option value="">Select Subcategory</option>';
    document.getElementById("form-container").innerHTML = "";
    document.getElementById("form-container").style.display = "none";
    document.getElementById("submit-button").style.display = "none";

    if (categoryName) {
      // Fetch subcategories via AJAX
      fetch(`/blog/?category=${categoryName}`)
        .then((response) => response.json())
        .then((data) => {
          subcategorySelect.style.display = "block";
          document.querySelector(
            'label[for="subcategory-select"]'
          ).style.display = "block";
          data.forEach(function (subcategory) {
            var option = document.createElement("option");
            option.value = subcategory.id;
            option.textContent = subcategory.name;
            subcategorySelect.appendChild(option);
          });
        });
    } else {
      subcategorySelect.style.display = "none";
      document.querySelector('label[for="subcategory-select"]').style.display =
        "none";
    }
  });

// Handle subcategory selection and load form fields
document
  .getElementById("subcategory-select")
  .addEventListener("change", function () {
    var subcategoryId = this.value;

    if (subcategoryId) {
      // Fetch form fields via AJAX
      fetch("", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
            .value,
        },
        body: `subcategory_id=${subcategoryId}`,
      })
        .then((response) => response.json())
        .then((formFields) => {
          var formContainer = document.getElementById("form-container");
          formContainer.innerHTML = "";
          formFields.forEach(function (field) {
            var label = document.createElement("label");
            label.textContent = field.label;
            var input = document.createElement("input");
            input.type = field.type;
            input.name = field.field_name;
            formContainer.appendChild(label);
            formContainer.appendChild(input);
          });
          formContainer.style.display = "block";
          document.getElementById("submit-button").style.display = "block";
        });
    } else {
      document.getElementById("form-container").style.display = "none";
      document.getElementById("submit-button").style.display = "none";
    }
  });
