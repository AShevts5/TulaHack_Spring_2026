function generate() {
  const role = document.getElementById("role").value;
  const disc = document.getElementById("disc").value;
  const motivation = document.getElementById("motivation").value;
  const generation = document.getElementById("generation").value;

  let profile = "";
  let communication = "";
  let risks = "";

  if (disc === "D") {
    profile = "Лидер, ориентирован на результат";
    communication = "Коротко и по делу";
    risks = "Может быть резким";
  }

  if (disc === "I") {
    profile = "Общительный и вдохновляющий";
    communication = "Дружелюбный стиль";
    risks = "Может отвлекаться";
  }

  if (disc === "S") {
    profile = "Надежный и стабильный";
    communication = "Спокойный тон";
    risks = "Сложно принимает изменения";
  }

  if (disc === "C") {
    profile = "Аналитичный и внимательный";
    communication = "Четкие инструкции";
    risks = "Перфекционизм";
  }

  let roleText = "";
  if (role === "Разработчик") roleText = "Работает с техническими задачами";
  if (role === "Менеджер") roleText = "Организует процессы и людей";
  if (role === "Аналитик") roleText = "Работает с данными и анализом";

  let motivationText = "";
  if (motivation === "Деньги") motivationText = "Бонусы и премии";
  if (motivation === "Рост") motivationText = "Развитие и обучение";
  if (motivation === "Стабильность") motivationText = "Спокойная рабочая среда";

  let generationText = "";
  if (generation === "Z") generationText = "Часто важны развитие и обратная связь";
  if (generation === "Y") generationText = "Часто важен баланс работы и жизни";
  if (generation === "X") generationText = "Часто важна стабильность и опыт";

  const resultBlock = document.getElementById("result");

const newHTML = `
  <div class="card"><b>Профиль:</b> ${profile}</div>
  <div class="card"><b>Роль:</b> ${roleText}</div>
  <div class="card"><b>Коммуникация:</b> ${communication}</div>
  <div class="card"><b>Мотивация:</b> ${motivationText}</div>
  <div class="card"><b>Риски:</b> ${risks}</div>
  <div class="card"><b>Особенности:</b> ${generationText}</div>
`;

if (resultBlock.classList.contains("show")) {
  resultBlock.classList.add("fade");

  setTimeout(() => {
    resultBlock.innerHTML = newHTML;
    resultBlock.classList.remove("fade");
  }, 200);

} else {
  resultBlock.innerHTML = newHTML;
  resultBlock.style.display = "block";

  setTimeout(() => {
    resultBlock.classList.add("show");
  }, 10);
 }
}