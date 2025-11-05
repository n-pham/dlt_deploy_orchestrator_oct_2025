from prefect import flow, task
import dlt


@task(log_prints=True)
def run_pipeline():

    import chess

    source = chess.source(["magnuscarlsen", "vincentkeymer", "dommarajugukesh", "rpragchess"])

    pipeline = dlt.pipeline(
        pipeline_name="chess_pipeline",
        destination="duckdb",
        dataset_name="chess_players_games_data",
        progress="log"
    )

    info = pipeline.run(source)
    print(info)
    return info

@flow(log_prints=True)
def main():

    github_workflow = run_pipeline()
    return github_workflow

if __name__ == "__main__":
    main.serve(
        name="my-first-deployment",
        cron="0 8 * * *"  # Run every day at 8:00 AM
    )