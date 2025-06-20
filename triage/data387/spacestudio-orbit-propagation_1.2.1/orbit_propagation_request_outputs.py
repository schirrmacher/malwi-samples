# coding: utf-8

"""
    Spacestudio Orbit Propagation API

    <b>CHANGELOG</b> <ul>   <li><b>1.2.0</b> - 2024-06-13 - Add <b>missionDuration</b> field in response payload</li>   <li><b>1.1.5</b> - 2024-06-06 - Improve API documentation</li>   <li><b>1.1.4</b> - 2024-05-28 - Improve API documentation</li>   <li><b>1.1.3</b> - 2024-05-28 - Improve API documentation</li>   <li><b>1.1.2</b> - 2024-05-28 - Improve API documentation</li>   <li><b>1.1.1</b> - 2024-05-28 - Delete <i>NONE</i> solar array type</li>   <li><b>1.1.0</b> - 2024-05-28 - Add perturbations and refactor API</li>   <li><b>1.0.0</b> - 2024-05-27 - Initial version</li> </ul> 

    The version of the OpenAPI document: 1.2.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from spacestudio_orbit_propagation.models.ephemeris_type import EphemerisType
from spacestudio_orbit_propagation.models.orbit_propagation_request_outputs_orbital_ephemerides import OrbitPropagationRequestOutputsOrbitalEphemerides
from spacestudio_orbit_propagation.models.orbit_propagation_request_outputs_spacecraft_states import OrbitPropagationRequestOutputsSpacecraftStates
from typing import Optional, Set
from typing_extensions import Self

class OrbitPropagationRequestOutputs(BaseModel):
    """
    Configuration of the expected orbit propagation computation outputs
    """ # noqa: E501
    orbital_ephemerides: Optional[OrbitPropagationRequestOutputsOrbitalEphemerides] = Field(default=None, alias="orbitalEphemerides")
    spacecraft_states: Optional[OrbitPropagationRequestOutputsSpacecraftStates] = Field(default=None, alias="spacecraftStates")
    ephemerides: Optional[List[EphemerisType]] = None
    ephemerides_step: Optional[StrictInt] = Field(default=None, description="The step of the ephemerides, in seconds", alias="ephemeridesStep")
    mean_ephemerides: Optional[StrictBool] = Field(default=None, description="Indicates whether the mean ephemerides should be computed", alias="meanEphemerides")
    osculating_ephemerides: Optional[StrictBool] = Field(default=None, description="Indicates whether the osculating ephemerides should be computed", alias="osculatingEphemerides")
    __properties: ClassVar[List[str]] = ["orbitalEphemerides", "spacecraftStates", "ephemerides", "ephemeridesStep", "meanEphemerides", "osculatingEphemerides"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OrbitPropagationRequestOutputs from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of orbital_ephemerides
        if self.orbital_ephemerides:
            _dict['orbitalEphemerides'] = self.orbital_ephemerides.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spacecraft_states
        if self.spacecraft_states:
            _dict['spacecraftStates'] = self.spacecraft_states.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrbitPropagationRequestOutputs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "orbitalEphemerides": OrbitPropagationRequestOutputsOrbitalEphemerides.from_dict(obj["orbitalEphemerides"]) if obj.get("orbitalEphemerides") is not None else None,
            "spacecraftStates": OrbitPropagationRequestOutputsSpacecraftStates.from_dict(obj["spacecraftStates"]) if obj.get("spacecraftStates") is not None else None,
            "ephemerides": obj.get("ephemerides"),
            "ephemeridesStep": obj.get("ephemeridesStep"),
            "meanEphemerides": obj.get("meanEphemerides"),
            "osculatingEphemerides": obj.get("osculatingEphemerides")
        })
        return _obj


