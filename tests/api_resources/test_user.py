# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from learnhub_sdk import LearnhubSdk, AsyncLearnhubSdk

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LearnhubSdk) -> None:
        user = client.user.create(
            body={
                "name": "test user",
                "email": "{{email}}",
            },
        )
        assert_matches_type(object, user, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LearnhubSdk) -> None:
        response = client.user.with_raw_response.create(
            body={
                "name": "test user",
                "email": "{{email}}",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LearnhubSdk) -> None:
        with client.user.with_streaming_response.create(
            body={
                "name": "test user",
                "email": "{{email}}",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: LearnhubSdk) -> None:
        user = client.user.retrieve()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: LearnhubSdk) -> None:
        user = client.user.retrieve(
            email="string",
        )
        assert_matches_type(object, user, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LearnhubSdk) -> None:
        response = client.user.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LearnhubSdk) -> None:
        with client.user.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LearnhubSdk) -> None:
        user = client.user.delete()
        assert_matches_type(str, user, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: LearnhubSdk) -> None:
        user = client.user.delete(
            email="string",
        )
        assert_matches_type(str, user, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: LearnhubSdk) -> None:
        response = client.user.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(str, user, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: LearnhubSdk) -> None:
        with client.user.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(str, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUser:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLearnhubSdk) -> None:
        user = await async_client.user.create(
            body={
                "name": "test user",
                "email": "{{email}}",
            },
        )
        assert_matches_type(object, user, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLearnhubSdk) -> None:
        response = await async_client.user.with_raw_response.create(
            body={
                "name": "test user",
                "email": "{{email}}",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLearnhubSdk) -> None:
        async with async_client.user.with_streaming_response.create(
            body={
                "name": "test user",
                "email": "{{email}}",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLearnhubSdk) -> None:
        user = await async_client.user.retrieve()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLearnhubSdk) -> None:
        user = await async_client.user.retrieve(
            email="string",
        )
        assert_matches_type(object, user, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLearnhubSdk) -> None:
        response = await async_client.user.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLearnhubSdk) -> None:
        async with async_client.user.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLearnhubSdk) -> None:
        user = await async_client.user.delete()
        assert_matches_type(str, user, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLearnhubSdk) -> None:
        user = await async_client.user.delete(
            email="string",
        )
        assert_matches_type(str, user, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLearnhubSdk) -> None:
        response = await async_client.user.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(str, user, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLearnhubSdk) -> None:
        async with async_client.user.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(str, user, path=["response"])

        assert cast(Any, response.is_closed) is True
