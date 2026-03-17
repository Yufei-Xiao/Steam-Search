import os
import csv
from sqlalchemy.exc import SQLAlchemyError

from . import db
from . import models


def parse_int(value):
    try:
        return int(value) if value != "" else None
    except ValueError:
        return None


def parse_float(value):
    try:
        return float(value) if value != "" else None
    except ValueError:
        return None


def import_csv(csv_path: str):
    db.Base.metadata.create_all(bind=db.engine)
    session = db.SessionLocal()
    inserted = 0
    try:
        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                game = models.Game(
                    appid=parse_int(row.get('appid', '').strip()),
                    name=row.get('name', '').strip(),
                    developer=row.get('developer', '').strip(),
                    publisher=row.get('publisher', '').strip(),
                    score_rank=parse_float(row.get('score_rank', '').strip()),
                    positive=parse_int(row.get('positive', '').strip()),
                    negative=parse_int(row.get('negative', '').strip()),
                    userscore=parse_float(row.get('userscore', '').strip()),
                    owners=row.get('owners', '').strip(),
                    average_forever=parse_int(row.get('average_forever', '').strip()),
                    average_2weeks=parse_int(row.get('average_2weeks', '').strip()),
                    median_forever=parse_int(row.get('median_forever', '').strip()),
                    median_2weeks=parse_int(row.get('median_2weeks', '').strip()),
                    price=parse_int(row.get('price', '').strip()),
                    initialprice=parse_int(row.get('initialprice', '').strip()),
                    discount=parse_int(row.get('discount', '').strip()),
                    ccu=parse_int(row.get('ccu', '').strip()),
                )
                # use merge to upsert based on primary key
                session.merge(game)
                inserted += 1
                if inserted % 500 == 0:
                    session.commit()
                    print(f"Imported {inserted} rows...")
            session.commit()
        print(f"Import complete. {inserted} rows processed.")
    except (IOError, SQLAlchemyError) as e:
        session.rollback()
        print("Error importing CSV:", e)
    finally:
        session.close()


if __name__ == '__main__':
    root = os.path.dirname(os.path.dirname(__file__))
    csv_path = os.path.join(root, 'data', 'steam_games_dataset.csv')
    if not os.path.exists(csv_path):
        print('CSV file not found at', csv_path)
    else:
        import_csv(csv_path)
