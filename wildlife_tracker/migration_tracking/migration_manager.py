from typing import Any, Optional

from wildlife_tracker.migration_tracking.migration import Migration
#from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class MigrationManager:

    def __init__(self):
        self.migrations: dict[int, Migration] = {}

    def schedule_migration(self, migration: Migration) -> None:
        self.migrations[migration.migration_id] = migration

    def cancel_migration(self, migration_id: int) -> None:
        if migration_id in self.migrations:
            del self.migrations[migration_id]

    def get_migration_by_id(self, migration_id: int) -> Migration:
        return self.migrations.get(migration_id)

    def get_migration_details(self, migration_id: int) -> dict[str, Any]:
        migration = self.get_migration_by_id(migration_id)
        return migration.__dict__ if migration else {}

    def get_migrations(self) -> list[Migration]:
        return list(self.migrations.values())
