import json
import os

class StudentRecordError(Exception):
    """Raised when a student record violates business rules."""
    pass

def validate_record(record, seen_ids):
    if not isinstance(record, dict):
        raise TypeError(f"Record is not a dictionary: {record}")

    required_fields = ["student_id", "name", "department", "marks"]
    for field in required_fields:
        if field not in record:
            raise StudentRecordError(f"missing required field '{field}'")

    student_id = record["student_id"]
    
    if not isinstance(student_id, str) or not student_id.strip():
        raise StudentRecordError("student_id must be non-empty string")
    
    if student_id in seen_ids:
        raise StudentRecordError(f"duplicate student_id '{student_id}'")

    marks = record["marks"]
    if not isinstance(marks, list):
        raise TypeError("marks must be a list")
    if len(marks) != 3:
        raise StudentRecordError(f"marks must contain exactly 3 values between 0 and 100, got {len(marks)}")

    for m in marks:
        if isinstance(m, bool): # bool is subclass of int
            raise StudentRecordError(f"boolean value not allowed as marks: {m}")
        if not isinstance(m, (int, float)):
            raise TypeError(f"marks must be numeric, found {type(m).__name__}: {m}")
        if not (0 <= m <= 100):
            raise ValueError(f"marks value {m} out of range (0-100)")
    return True

def main():
    input_file = input("Enter input file path [students_input.json]: ").strip() or "students_input.json"
    valid_output = "students_valid.json"
    error_log = "import_errors.txt"

    print(f"\nImport started: {input_file}")

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file not found: {input_file}")
        with open(error_log, 'w', encoding='utf-8') as ef:
            ef.write(f"File error: FileNotFoundError - {input_file} not found\n")
        return
    except PermissionError:
        print(f"Error: Permission denied: {input_file}")
        with open(error_log, 'w', encoding='utf-8') as ef:
            ef.write(f"File error: PermissionError - {input_file}\n")
        return
    except OSError as e:
        print(f"Error: OS error: {e}")
        return
    except json.JSONDecodeError as e:
        print(f"Error: Malformed JSON: {e}")
        with open(error_log, 'w', encoding='utf-8') as ef:
            ef.write(f"JSON parsing error: {e} at line {e.lineno}\n")
        return
    else:
        print("File parsed successfully.")
        if not isinstance(data, list):
            print("Error: JSON root must be a list")
            return

    valid_records = []
    errors = []
    seen_ids = set()

    try:
        for idx, rec in enumerate(data, start=1):
            try:
                validate_record(rec, seen_ids)
            except (StudentRecordError, ValueError, TypeError, KeyError) as e:
                msg = f"Rejected record {idx}: {e}"
                print(msg)
                errors.append(msg)
                continue
            else:
                seen_ids.add(rec["student_id"])
                valid_records.append(rec)
                print(f"Accepted: {rec['student_id']} - {rec['name']}")
    finally:
        print("\n--- Processing Finished ---")

    try:
        with open(valid_output, 'w', encoding='utf-8') as out:
            json.dump(valid_records, out, indent=2)
        with open(error_log, 'w', encoding='utf-8') as ef:
            ef.write("\n".join(errors) if errors else "No errors\n")
    except OSError as e:
        print(f"Error writing output: {e}")
        return

    print("\nImport completed.")
    print(f"Accepted records: {len(valid_records)}")
    print(f"Rejected records: {len(errors)}")
    print(f"Valid output: {valid_output}")
    print(f"Error log: {error_log}")

if __name__ == "__main__":
    main()