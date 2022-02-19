"""UpdateAuditLogsTable Migration."""

from masoniteorm.migrations import Migration


class CreateAuditLogsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("audit_logs") as table:
            table.uuid('id')
            table.string('auditable')
            table.string('event')
            table.big_integer('auditable_id')
            table.jsonb('old_values')
            table.jsonb('new_values')
            table.big_integer('user_id').nullable()
            table.timestamps()

            table.primary('id')
            table.foreign('user_id').references('id').on('users')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("audit_logs")
