from gym.envs.registration import register

register(
    id='AirSimMultirotor-v0',
    entry_point='airsim_gym.envs:AirSimMultirotor',
)
