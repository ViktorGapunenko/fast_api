from sqlalchemy import select
from database import TaskEntity, new_session
from model import TaskAddModel


class TaskRepository:

    @classmethod
    async def add_one(cls, data: TaskAddModel) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskEntity(**task_dict)

            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(TaskEntity)
            result = await session.execute(query)
            tasks_models = result.scalars().all()
            return tasks_models
