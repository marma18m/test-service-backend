from fastapi import APIRouter, HTTPException
import yaml
from starlette import status
from schemas.errors import BAD_REQUEST

router = APIRouter(
    prefix="/initial_load",
    tags=["frontend service"],
)


@router.get(
    "/load",
    status_code=status.HTTP_200_OK,
    responses={**BAD_REQUEST},
)
async def load_initial_data():
    """
    Load initial data for the frontend service.
    """
    try:
        with open("config.yaml", "r") as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Configuration file not found",
        )
    except yaml.YAMLError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error parsing YAML file: {e}",
        )

    if "VisionSystem" not in config or "device" not in config["VisionSystem"]:
        raise HTTPException(
            status_code=500,
            detail="Invalid configuration file format",
        )

    devices = config["VisionSystem"]["device"]
    cameras = []
    for device in devices:
        if "camera" in device:
            cam = {"name": device["name"], "enable": device["enable"]}
            cameras.append(cam)

    return {"type": config["VisionSystem"]["type"], "cameras": cameras}
