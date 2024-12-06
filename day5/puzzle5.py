def build_rule_dict(rules_input: [str]) -> {int: [int]}:
    rules_dict = {}
    for rule in rules_input:
        rule = rule.split("|")
        rule_for_number = int(rule[1])
        if rule_for_number not in rules_dict:
            rules_dict[rule_for_number] = []
        rules_dict[rule_for_number].append(int(rule[0]))
    return rules_dict

def check_job(pages_in_job: [int], rules_dict: {int: [int]}) -> bool:
    job_valid = True

    page_counter = 0
    while job_valid and page_counter < len(pages_in_job):
        current_rules = rules_dict.get(pages_in_job[page_counter], [])
        pages_after = pages_in_job[page_counter:]
        job_valid = not any(page_num in pages_after for page_num in current_rules)
        page_counter += 1
    return job_valid

def main():
    with open("puzzle_input.txt") as f:
        printer_input = f.read().split("\n\n")

    rules_input = printer_input[0].strip().split("\n")
    print_jobs = printer_input[1].strip().split("\n")

    rules_dict = build_rule_dict(rules_input)
    total = 0

    for job in print_jobs:
        pages_in_job = [int(page) for page in job.strip().split(",")]
        if check_job(pages_in_job, rules_dict):
            middle_element = int((len(pages_in_job) / 2))
            total += pages_in_job[middle_element]
    print(total)


if __name__ == "__main__":
    main()
