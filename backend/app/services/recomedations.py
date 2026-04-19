from __future__ import annotations

def _dominant_disc(disc: dict[str, int]) -> str:
    keys = ("D", "I", "S", "C")
    parts = {k: int(disc.get(k, 0)) for k in keys}
    total = sum(parts.values()) or 1
    normed = {k: parts[k] / total for k in keys}
    return max(normed, key=normed.get)

def build_recommendations(criteria: dict) -> dict:
    mode = criteria.get("mode") or "hire"
    role = criteria.get("role") or "Сотрудник"
    disc = criteria.get("disc") or {}
    motivation = criteria.get("motivation") or []
    generation = criteria.get("generation")
    team_ctx = (criteria.get("team_context") or "").strip()
    mgr = (criteria.get("manager_notes") or "").strip()

    dom = _dominant_disc(disc) if isinstance(disc, dict) else "S"
    mot_txt = ", ".join(motivation) if motivation else "не указаны явно — уточните на 1:1"

    candidate_profile = [
        f"Роль в команде: ориентир на «{role}».",
        f"По DISC доминирует «{dom}»: подберите человека, который усиливает команду в зоне {dom}, "
        f"и закрывает пробелы по остальным осям через парную работу/процессы.",
        "Формат работы: чёткие критерии готовности, короткие циклы обратной связи, прозрачные приоритеты.",
    ]

    if mode == "hire":
        candidate_profile.append(
            "Для подбора: заложите 2–3 поведенческих интервью по кейсам + проверку мотивационного совпадения с задачами."
        )
    else:
        candidate_profile.append(
            "Для действующего состава: не «ищем идеального», а «снимаем трение»: договоритесь о правилах коммуникации и ритме синков."
        )

    onboarding = [
        "Первые 3 дня: контекст цели команды, глоссарий, доступы, «кто за что отвечает».",
        "Первая неделя: 2 коротких 1:1 (15–20 мин) — ожидания, риски, что помогает/мешает.",
        "Вторая неделя: первый мини-результат в прод/демо + ретро на процесс, не на людей.",
    ]

    one_on_one = [
        "Фиксируйте повестку заранее (3 пункта максимум).",
        "30% времени — статус; 70% — снятие блокеров и согласование решений.",
        f"Мотивация по вводным: {mot_txt}.",
    ]

    motivation_conditions = [
        "Связывайте задачи со смыслом и видимым вкладом (даже внутренние релизы — «для кого стало лучше»).",
        "Договоритесь о границах автономии: где нужна согласованность, где можно решать самостоятельно.",
        "Избегайте «награды только деньгами» как единственного рычага — добавляйте рост, ответственность, инструменты.",
    ]

    if generation:
        motivation_conditions.append(
            f"Поколение «{generation}»: не опирайтесь на стереотипы; спросите напрямую про формат обратной связи, "
            f"гибкость и критерии успеха — и зафиксируйте это письменно."
        )

    risks = [
        "Риск: перегруз синками — введите асинхронные статусы и правило «по умолчанию пишем, созваниваемся если не сходится за N часов».",
        "Риск: размытые роли — RACI/ответственный за решение на каждый тип задачи.",
    ]

    if team_ctx:
        risks.append(f"Контекст команды учтён: {team_ctx[:280]}{'…' if len(team_ctx) > 280 else ''}")

    if mgr:
        risks.append(f"Заметки руководителя: {mgr[:280]}{'…' if len(mgr) > 280 else ''}")

    return {
        "title": "Рекомендации Team Builder",
        "candidate_profile": candidate_profile,
        "onboarding_2_weeks": onboarding,
        "one_on_one": one_on_one,
        "motivation_conditions": motivation_conditions,
        "risks_and_mitigations": risks,
    }
