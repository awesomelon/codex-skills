I recommend keeping the in-process queue provisionally, with a move to a managed queue if accepted jobs must survive process restarts.

| Option | Benefit | Tradeoff |
| --- | --- | --- |
| Keep the in-process queue | Retains the current setup without another service or its ongoing cost. | The supplied design confirms that queued jobs are lost on restart. Suitable only if that loss is acceptable or jobs can reliably be recreated. |
| Move to a managed queue | A service with durable storage can preserve pending jobs across application restarts. | Adds cost and a service dependency. Its persistence, delivery, retry, and duplicate-handling requirements need verification before adoption. |

The design does not establish a durability requirement, job recovery mechanism, workload, or budget, so there is not enough evidence to justify migration yet. The recommendation changes if lost jobs cause missed obligations or cannot be recovered: in that case, favor a durable managed queue and verify recovery after a worker restart before rollout.

This is a design-only assessment; I did not edit the workspace or test a queue implementation.

Can queued jobs be safely lost or recreated after a restart, or must every accepted job survive?
